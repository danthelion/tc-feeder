# Camel training and feeding action

This GitHub Action will train your camel and feed it. Schedule it to run every day.

Requires to secrets to be set:

- `TC_USER`: Your TC username
- `TC_PASSWORD`: Your TC password

Example workflow:

```yaml
name: feed & train camel

on:
  schedule:
    - cron: '0 9 * * *'
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:

      - name: checkout repo content
        uses: actions/checkout@v2

      - name: Feed and train 🐪
        uses: danthelion/tc-feeder
        env:
          TC_USER: ${{ secrets.TC_USER }}
          TC_PASSWORD: ${{ secrets.TC_PASSWORD }}
```