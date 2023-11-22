# Secure Coding with LLMs

## Seting up the Environment

Add your openAI API key in an environment variable and install all the dependencies.

```bash
export OPENAI_API_KEY=openai-api-key
pip install -r requirements
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

## Running the Pipeline

```bash
python pipeline.py
```

The first step of the pipeline is to enter a filename that contains the vulnerable code that you would like to be fixed.

```bash
The file that contains vulnerable code:
```

The next user input is contextual code.

```bash
Do you have any contextual code (y/n)
```

If you enter `y` you will then be prompted to enter the contextual code.

```bash
The code in plaintext:
```

The last thing you have to input is the consequences of insecure code.

```bash
What are the consequences if the code is not secure?
```
