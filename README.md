
### **AWS VPC Visualizer** 🕵️‍♀️✨  
Because who doesn’t love a good cloud architecture diagram? And, darling, if you don’t visualize your VPC, do you even have one?  

---

## **💻 About**  
Ever found yourself drowning in a sea of AWS VPCs, desperately trying to make sense of your cloud infrastructure? Fear not, because **AWS VPC Visualizer** is here to *spill the tea* ☕ and lay it all out for you—visually.  

> *And why all the drama in this intro, you ask? Because, sweetheart, Gossip Girl is always here to guide you—and to make sure you stay one step ahead.* 💋  

<p align="center">
  <img width="400" src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZ2ZmejExZDhlYWNvanB4aHUxano4MGppYWNncGRxOHQwYWloY3BicCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/pFJJkgTMKlwiI/giphy.gif">
</p>  

This CLI tool will fetch your VPC details, let you pick one, and generate a **fabulous** network diagram. All with the elegance of a well-orchestrated Upper East Side soirée.  

---

## **✨ Features**  
- Lists **all** your AWS VPCs (because choice is power).  
- Allows you to **select** a VPC and visualize **all** its components.  
- Supports **Internet Gateways, NAT Gateways, Subnets, Load Balancers, Route Tables** & more.  
- Outputs **a sleek, clean network diagram** that even Blair Waldorf would approve of.  

---

## **📦 Prerequisites**  
Before you strut your way into AWS cloud visualization, make sure your system is **red carpet-ready**:  

### **1️⃣ Install Python & Virtual Environment**  
First, darling, make sure you have Python installed (preferably **Python 3.10+**). If you don’t:  
```bash
sudo apt install python3 python3-venv python3-pip  # Ubuntu
brew install python  # macOS
```

### **2️⃣ Install Graphviz (The Secret Weapon)**  
This tool is the heartbeat of your diagrams. No Graphviz? No AWS architecture drama.  
```bash
brew install graphviz  # macOS (Homebrew)
sudo apt install graphviz  # Ubuntu/Debian
```

### **3️⃣ Set Up Your Virtual Environment**  
Create and activate your own cozy Python environment—because working directly on your system? So *déclassé*.  
```bash
python3 -m venv venv  
source venv/bin/activate  # On macOS/Linux  
venv\Scripts\activate  # On Windows  
```

### **4️⃣ Install the Required Python Packages**  
Like every good socialite, your Python environment needs a few essentials:  
```bash
pip install -r requirements.txt
```
or, manually:
```bash
pip install boto3 diagrams
```

---

## **🚀 Running the AWS VPC Visualizer**  
Now that you’re all set, let’s get to the fun part:  
```bash
python3 aws_vpc_visualizer.py
```
What happens next? You’ll see a **list of your VPCs**, and it’s time to **choose one**—carefully, of course.  

---

## **💡 How to Use**  
1️⃣ **Pick Your VPC:** The script will display all available VPCs, complete with their **IDs** and **CIDR blocks**.  
2️⃣ **Type the Number:** Just enter the **number** of the VPC you want to visualize.  
3️⃣ **Enjoy the Magic:** The script will generate a **beautiful** architecture diagram of your VPC, right before your eyes. ✨  

💡 **Pro Tip:** Don’t want to choose? Type **'q'** to gracefully exit, like the true AWS connoisseur you are.  

---

## **📷 Sample Output**  
*Coming soon—because every icon deserves a photoshoot.* 📸  

---

## **⚠️ Troubleshooting**  
> **Error:** `ModuleNotFoundError: No module named 'diagrams'`  
💡 **Fix:** You probably forgot to install the dependencies. Just run:  
```bash
pip install -r requirements.txt
```

> **Error:** `graphviz.backend.execute.ExecutableNotFound: failed to execute PosixPath('dot')`  
💡 **Fix:** You need to install **Graphviz**. Run:  
```bash
brew install graphviz  # macOS  
sudo apt install graphviz  # Ubuntu  
```

> **Error:** `botocore.exceptions.NoCredentialsError: Unable to locate credentials`  
💡 **Fix:** Set up your AWS credentials:  
```bash
aws configure
```

---

## **🌎 Future Plans**  
- 🎨 **Flask/FastAPI Web Interface** (because CLI is *so last season*).  
- 📊 **More AWS Services** (Load Balancers, Route 53, VPN Gateways).  
- 💸 **Monetization? Maybe.** (Would Blair Waldorf give this away for free? 🤔).  

---

## **🎭 License**  
This project is licensed under the **MIT License**, because **sharing is caring**—but if you steal this and start charging for it, just know **I’ll find out**. XOXO 💋  

---

**💌 Questions? Requests? AWS Secrets to Share?**  
Drop me a line at **GitHub Issues** or send a carrier pigeon. 🕊  

---

That’s it, darlings. Now go forth and visualize like an **AWS Queen**.  
**XOXO, AWS VPC Visualizer.** 😘  

---
