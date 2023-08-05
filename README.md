# TeveClub camel training and feeding action

This GitHub Action will train your camel and feed it. Schedule it to run every day for best results.

Requires two input variables:

- `TC_USER`: Your TC username
- `TC_PASSWORD`: Your TC password

Example workflow definition with secrets and a schedule to run every day at 9am, and allow manual triggering:

```yaml
name: Daily 🐪 training and feeding

on:
  schedule:
    - cron: '0 9 * * *'
  workflow_dispatch:

jobs:
  feed-and-train:
    runs-on: ubuntu-latest
    steps:

      - name: Feed and train 🐪
        uses: danthelion/tc-feeder@v2
        with:
          tc_user: ${{ secrets.TC_USER }}
          tc_password: ${{ secrets.TC_PASSWORD }}
```
