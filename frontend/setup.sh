#!/bin/bash
cd /home/explorer
yarn install
yarn build

exec "$@"
