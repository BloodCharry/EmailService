#!/bin/sh
until redis-cli -h redis ping; do
  echo "Waiting for Redis..."
  sleep 5
done
exec "$@"