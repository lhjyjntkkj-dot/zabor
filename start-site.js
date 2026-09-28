/**
 * start-site.js — запуск сайта CH PROJECT на своём компьютере.
 *
 * Зачем нужен: страницы подключают стили и скрипты по адресам вида
 * /css/styles.css. Если открыть index.html двойным кликом, браузер
 * такие адреса не найдёт и сайт развалится. Этот файл поднимает
 * настоящий веб-сервер, и всё работает как в интернете.
 *
 * Дополнительно перенаправляет заявки (/api/...) на сервер приёма
 * заявок, если он запущен на порту 3001.
 *
 * Запуск:  node start-site.js
 * Открыть: http://localhost:8080
 * Остановить: Ctrl + C
 *
 * Никаких библиотек не требует — работает на чистом Node.js.
 */

const http = require("http");
const fs = require("fs");
const path = require("path");

const PORT = process.env.SITE_PORT || 8080;
const API_PORT = process.env.PORT || 3001;
const ROOT = __dirname;

const TYPES = {
  ".html": "text/html; charset=utf-8",
  ".css": "text/css; charset=utf-8",
  ".js": "application/javascript; charset=utf-8",
  ".json": "application/json; charset=utf-8",
  ".png": "image/png",
  ".jpg": "image/jpeg",
  ".jpeg": "image/jpeg",
  ".webp": "image/webp",
  ".svg": "image/svg+xml",
  ".ico": "image/x-icon",
  ".woff2": "font/woff2",
  ".woff": "font/woff",
};

/** Перенаправляем заявки на backend (api/server.js) */
function proxyToApi(req, res) {
  const body = [];
  req.on("data", (c) => body.push(c));
  req.on("end", () => {
    const data = Buffer.concat(body);
    const proxyReq = http.request(
      {
        host: "127.0.0.1",
        port: API_PORT,
        path: req.url,
        method: req.method,
        headers: { ...req.headers, host: `127.0.0.1:${API_PORT}`, "content-length": data.length },
      },
      (proxyRes) => {
        res.writeHead(proxyRes.statusCode, proxyRes.headers);
        proxyRes.pipe(res);
      }
    );

    proxyReq.on("error", () => {
      // Сервер приёма заявок не запущен — говорим об этом понятным языком
      res.writeHead(503, { "Content-Type": "application/json; charset=utf-8" });
      res.end(
        JSON.stringify({
          ok: false,
          error:
            "Сервер приёма заявок не запущен. Откройте второе окно команд, " +
            "перейдите в папку api и выполните: npm run all",
        })
      );
    });

    proxyReq.end(data);
  });
}

const server = http.createServer((req, res) => {
  const url = decodeURIComponent(req.url.split("?")[0]);

  if (url.startsWith("/api/")) return proxyToApi(req, res);

  let rel = url === "/" ? "/index.html" : url;
  if (!path.extname(rel)) rel += ".html"; // /contacts -> /contacts.html

  // защита от выхода за пределы папки сайта
  const filePath = path.join(ROOT, rel);
  if (!filePath.startsWith(ROOT)) {
    res.writeHead(403);
    return res.end("Доступ запрещён");
  }

  fs.readFile(filePath, (err, data) => {
    if (err) {
      res.writeHead(404, { "Content-Type": "text/html; charset=utf-8" });
      return res.end(
        `<h1>404 — страница не найдена</h1>
         <p>Файл <code>${rel}</code> отсутствует.</p>
         <p><a href="/">На главную</a></p>`
      );
    }
    res.writeHead(200, {
      "Content-Type": TYPES[path.extname(filePath)] || "application/octet-stream",
      "Cache-Control": "no-cache", // чтобы сразу видеть правки
    });
    res.end(data);
  });
});

server.on("error", (err) => {
  if (err.code === "EADDRINUSE") {
    console.error(`\n❌ Порт ${PORT} уже занят.`);
    console.error("   Либо сайт уже запущен в другом окне, либо порт занят другой программой.");
    console.error(`   Можно запустить на другом порту:  SITE_PORT=8081 node start-site.js\n`);
  } else {
    console.error("Ошибка сервера:", err.message);
  }
  process.exit(1);
});

server.listen(PORT, () => {
  console.log("");
  console.log("  ✅ Сайт CH PROJECT запущен");
  console.log("");
  console.log(`  Откройте в браузере:  http://localhost:${PORT}`);
  console.log("");
  console.log("  Остановить: Ctrl + C");
  console.log("");
});
