# SERPOutreacher

A simple CLI tool to search for 'Write for us' opportunities based on a given keyword.

## Requirements

- Python 3.x
- pip

## Installation

`pip install git+https://github.com/mrizwan47/serp-outreach-finder.git`

## Usage

```bash
serpo [keyword] -o [output_file] -n [num_results]
```

- `keyword`: The keyword you want to search for.
- `output_file` (optional): The file where search results will be saved. Default is `results.csv`.
- `num_results` (optional): Number of results to fetch (range 10-100). Default is 100.

## Examples

1. `serpo "content marketing"`
2. `serpo "content marketing" -o marketing_results.csv`
3. `serpo "content marketing" -o marketing_results.csv -n 50`


## Disclaimer
This software is provided "as-is" without any warranty of any kind, either expressed or implied, including but not limited to the implied warranties of merchantability and fitness for a particular purpose. The authors and maintainers are not responsible for any damages, data loss, or legal repercussions that may occur from the use of this software.

This tool is intended solely for educational and research purposes. Web scraping Google Search is against Google's terms of service, and users should be aware that Google could block their IP address or take other actions if they are caught scraping search results.

By using this software, you agree to indemnify and hold harmless the authors and maintainers from any claims, actions, suits, losses, costs, charges, penalties, damages, liabilities, and expenses, including reasonable attorneys' fees, arising out of any use or misuse of this software.

Use of this software should comply with all applicable laws and regulations. The authors and maintainers of this software do not condone or endorse any illegal or unethical activities related to the use of this software. By using this tool, you acknowledge that you have read and understood this disclaimer and agree to abide by all the mentioned terms.
