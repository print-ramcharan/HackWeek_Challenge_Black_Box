content = """
# Black Box Challenge – COSC Hackweek

This project is my solution to the **Black Box Challenge**, where the goal was to reverse-engineer unknown API endpoints by experimenting and documenting their behavior. I then recreated the same behavior using **FastAPI**.

---

## 🚀 How I approached this challenge

I started by testing the provided cloud endpoints with a variety of `curl` commands and different JSON payloads. For each endpoint, I tried strings, numbers, empty values, and special characters. I carefully noted the outputs and looked for patterns. Some endpoints were straightforward (like Base64 encoding), while others had tricky conditions (like returning random permutations or enforcing character checks).

Once I was confident about how each endpoint worked, I implemented them locally in Python using FastAPI. I also created a set of shell scripts and curl examples to re-verify that my implementation produced identical outputs.

---

## 🧩 Endpoint Documentation

Below is a description of each endpoint and example commands you can use to test them.

---

### 1️⃣ /data
**Description:** Returns the Base64 encoding of the input string.

#### Example request:
\`\`\`bash
curl -X POST "http://127.0.0.1:8000/data" \\
  -H "Content-Type: application/json" \\
  -d '{"data":"hello"}'
\`\`\`

#### Example response:
\`\`\`json
{"result":"aGVsbG8="}
\`\`\`

---

### 2️⃣ /time
**Description:** Returns a decreasing integer value each time it is called.

#### Example request:
\`\`\`bash
curl -X GET "http://127.0.0.1:8000/time"
\`\`\`

#### Example response:
\`\`\`json
{"result":8158545}
\`\`\`

---

### 3️⃣ /fizzbuzz
**Description:** Always returns \`false\`, no matter what input is provided.

#### Example request:
\`\`\`bash
curl -X POST "http://127.0.0.1:8000/fizzbuzz" \\
  -H "Content-Type: application/json" \\
  -d '{"data":"15"}'
\`\`\`

#### Example response:
\`\`\`json
{"result":false}
\`\`\`

---

### 4️⃣ /glitch
**Description:**
- If the input string has **even length**, returns a random permutation of the characters.
- If the input string has **odd length**, returns the reversed string.

#### Example requests:
Even-length string:
\`\`\`bash
curl -X POST "http://127.0.0.1:8000/glitch" \\
  -H "Content-Type: application/json" \\
  -d '{"data":"12"}'
\`\`\`
Example responses:
\`\`\`json
{"result":"21"}
\`\`\`
or
\`\`\`json
{"result":"12"}
\`\`\`

Odd-length string:
\`\`\`bash
curl -X POST "http://127.0.0.1:8000/glitch" \\
  -H "Content-Type: application/json" \\
  -d '{"data":"abc"}'
\`\`\`
Example response:
\`\`\`json
{"result":"cba"}
\`\`\`

---

### 5️⃣ /alpha
**Description:** Returns \`true\` if the string starts with an alphabet character. Otherwise, returns \`false\`.

#### Example requests:
Starts with an alphabet:
\`\`\`bash
curl -X POST "http://127.0.0.1:8000/alpha" \\
  -H "Content-Type: application/json" \\
  -d '{"data":"hello123"}'
\`\`\`
Response:
\`\`\`json
{"result":true}
\`\`\`

Starts with a number:
\`\`\`bash
curl -X POST "http://127.0.0.1:8000/alpha" \\
  -H "Content-Type: application/json" \\
  -d '{"data":"1hello"}'
\`\`\`
Response:
\`\`\`json
{"result":false}
\`\`\`

---

### 6️⃣ /zap
**Description:** Returns the input string with all numeric characters removed.

#### Example request:
\`\`\`bash
curl -X POST "http://127.0.0.1:8000/zap" \\
  -H "Content-Type: application/json" \\
  -d '{"data":"a1b2c3"}'
\`\`\`

#### Example response:
\`\`\`json
{"result":"abc"}
\`\`\`

---

## 💻 How to run this project locally

1. **Clone the repository**
   \`\`\`bash
   git clone <your-repo-url>
   cd <your-repo-folder>
   \`\`\`

2. **Create a virtual environment**
   \`\`\`bash
   python3 -m venv venv
   source venv/bin/activate
   \`\`\`

3. **Install dependencies**
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

4. **Start the server**
   \`\`\`bash
   uvicorn main:app --reload
   \`\`\`

5. **Test endpoints**
   You can use the example curl commands above or run the scripts inside \`test_scripts/\`.

---

## 🧪 How I tested each endpoint

I created a set of shell scripts that cover all the known cases. For more thorough verification, I manually ran additional curl commands with different edge cases (empty strings, special characters, numbers) to confirm behavior.

---

## 🙌 Credits
Thanks to the COSC Hackweek team for designing a unique and challenging task.

Feel free to explore or adapt this code!
"""

with open("README.md", "w") as f:
    f.write(content.strip())

print("README.md created successfully.")
