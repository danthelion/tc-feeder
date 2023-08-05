# TeveClub camel training and feeding action

This GitHub Action will train your camel and feed it. Schedule it to run every day for best results.

Requires two input variables:

- `tc_user`: Your TeveClub username
- `tc_password`: Your TeveClub password

Example workflow definition with GitHub Actions Secrets and a schedule to run every day at 9am.

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
        uses: danthelion/tc-feeder@v3
        with:
          tc_user: ${{ secrets.TC_USER }}
          tc_password: ${{ secrets.TC_PASSWORD }}
```
