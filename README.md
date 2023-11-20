## Setup

```bash
pip install -r requirements
python pipeline.py
```

### Static Analysis Tools

#### [Flawfinder](https://dwheeler.com/flawfinder/)

For `C/C++`, already installed with `pip`.

#### [Bandit](https://bandit.readthedocs.io/en/latest/)

For `Python`, already installed with `pip`.

#### [Spotbugs](http://spotbugs.readthedocs.io/en/latest/)

For `Java`, download the zip file from [the official manual](https://spotbugs.readthedocs.io/en/latest/installing.html) and unzip it.

#### [Bearer](https://docs.bearer.com)

Most of its security rules are for `JavaScript/TypeScript`, run the following command or see [the instructions](https://docs.bearer.com/reference/installation/) for other install method.

```bash
curl -sfL https://raw.githubusercontent.com/Bearer/bearer/main/contrib/install.sh | sh
```
