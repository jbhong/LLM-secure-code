import re
from openai import OpenAI
import subprocess
from colorama import Fore

client = OpenAI()


def main():
    # has_contextual_code = input(
    # Fore.MAGENTA + "\nDo you have any contextual code (y/n) "
    # ).lower()
    has_contextual_code = "n"
    contextual_code = ""
    if has_contextual_code == "y":
        contextual_code = input("The code in plaintext:\n")
        contextual_code = f"This is code that will be relevant\n```{contextual_code}```"
    # consequences = input("What are the consequences if the code is not secure? ")
    
    vulnerable_file = input("Enter the filename to check for vulnerabilities:\n")
    print()

    print("*** Statis Analysis of the code... ***")
    [filename, extension] = vulnerable_file.split(".")
    code = open(vulnerable_file).read()
    code = static_analyse_code(filename, extension, code)
    print("*** Statis Analysis completed ***")
    print()

    response = (
        client.chat.completions.create(model="gpt-4",
        messages=[
            {
                "role": "user",
                "content": f"""
            Give me an overview of the functionality of the following code all in one paragraph. Do not mention any specific function calls or system calls. Detect any vulnerabilities and note any CWE number or CVE ID if they are known.
            ```
            {code}
            ```
            """,
            }
        ])
        .choices[0]
        .message.content
    )

    overview = response.split("\n")[0]
    print(Fore.YELLOW + overview, end="\n\n")

    fix = input(Fore.MAGENTA + "Do you wish to revise/fix your code? (y/n): ").lower() == "y"
    iteration = 1
    generated = False
    vul = ""
    while fix:
        generated = True
        code, vul = codecheck(code, overview, has_contextual_code, contextual_code, iteration, vul)
        fix = input(Fore.MAGENTA + "Do you wish to further revise/fix your code? (y/n): ").lower() == "y"
        iteration += 1

    if generated:
        save_code(code, filename, extension, iteration)
        print(Fore.GREEN + f"You have revised your code {iteration - 1} times")
        print(Fore.GREEN + f"Your final code is available in the file updated_{filename}.{extension}")
    else:
        print(Fore.GREEN + f"Your code is unmodified.")



def save_code(code, filename, extension, iteration):
    # print("AAAAAAAAA")
    # print(code)
    # print("AAAAAAAAA")
    if iteration > 0:
        #remove the first line from the code
        code = "\n".join(code.split("\n")[1:]).strip()
    # print("BBBBBBBBB")
    # print(code)
    # print("BBBBBBBBB")
    with open(f"updated_{filename}.{extension}", "w") as file:
        file.write(code)



def static_analyse_code(filename: str, extension: str, code: str):
    match extension:
        case "c":
            tool = ["flawfinder"]
        case "cpp":
            tool = ["flawfinder"]
        case "cxx":
            tool = ["flawfinder"]
        case "cc":
            tool = ["flawfinder"]
        case "java":
            filename = re.findall("public class (\w+)", code)[0]
            with open(f"{filename}.java", "w") as file:
                file.write(code)
            subprocess.run(["javac", f"{filename}.java"])
            subprocess.run(
                ["java", "-jar", "spotbugs-4.8.1/lib/spotbugs.jar", f"{filename}.class"])
            return
        case "py":
            tool = ["bandit"]
        case "js":
            tool = ["bin/bearer", "scan"]
        case "ts":
            tool = ["bin/bearer", "scan"]
        case _:
            return
        
    subprocess.run([*tool, f"{filename}.{extension}"])
    return code




def codecheck(code, overview, has_contextual_code, contextual_code, iteration, vul=""):
    messages = [
        {
            "role": "system",
            "content": "You are a secure code generation assistant. You are to generate code based on a overview of the functionality, in the language based on the extension provided. Do not generate any comments or code formatting just give me the code itself in plaintext. Focus on security, make sure you adhere to all secure coding guidelines.",
        },
        {
            "role": "user",
            "content": f"there may be a vulnerability in the code. The vulnerability is {vul}. I would like to revise the code to remove the vulnerability. Here is the code:"
            f"""
            ```
            {code}
            ```
            """
            f"""If so, explain the details of the vulnerability and then regenerate it without changing the functionality of the code but with the vuerabilities removed. Make sure it has the following functionality: {overview}
            """
            "This is a contenxtual code that will be relevant (if any): "
            f"{contextual_code if has_contextual_code == 'y' else ''}",
        },
    ]

    response = (
        client.chat.completions.create(model="gpt-4", messages=messages)
        .choices[0]
        .message.content
    )

    print(Fore.YELLOW + response, end="\n\n")
    code = Fore.CYAN + re.findall("```(.*?)```", response, re.DOTALL)[0].strip().strip('`')
    return code, response


if __name__ == "__main__":
    main()


# oobr.c
# CWE-125
# https://cwe.mitre.org/data/definitions/125.html



# sidechannel.c
# CVE-2024-25191
# CWE-203 observable discrepancy
# strcmp in authentication, prone to timining side channel.
# https://www.cvedetails.com/cve/CVE-2024-25191/



# bur.c
# CVSS-2024-25629
# CWE-127 buffer under-read
# solution: https://github.com/c-ares/c-ares/commit/a804c04ddc8245fc8adf0e92368709639125e183
# /* Probably means there was an embedded NULL as the first character in
#  * the line, throw away line */
# if (len == 0) {
#   offset = 0;
#   continue;
# }

