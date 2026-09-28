#!/bin/bash
cd "$(dirname "$0")"
if ! command -v node >/dev/null 2>&1; then
  echo ""
  echo "  ОШИБКА: не установлен Node.js"
  echo "  Зайдите на nodejs.org, установите, перезагрузите компьютер."
  echo ""
  read -n 1
  exit 1
fi
echo ""
echo "  Запускаю сайт..."
echo ""
(sleep 2 && open http://localhost:8080) &
node start-site.js
