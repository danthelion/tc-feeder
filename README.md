# Camel training and feeding action

This GitHub Action will train your camel and feed it. Schedule it to run every day.

Requires two environment variables:

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
  feed-and-train:
    runs-on: ubuntu-latest
    steps:

      - name: Feed and train 🐪
        uses: danthelion/tc-feeder@0.4
        env:
          TC_USER: ${{ secrets.TC_USER }}
          TC_PASSWORD: ${{ secrets.TC_PASSWORD }}
```