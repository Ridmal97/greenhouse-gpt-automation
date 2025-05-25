# 🌿 Greenhouse GPT Automation

This project, **greenhouse-gpt-automation**, is a smart greenhouse management system that combines **Embedded AI**, **IoT**, and **ChatGPT API** to fully automate environmental monitoring and control in agricultural setups.

---

## 🚀 Features

- 📡 ESP32-based real-time sensor data collection (temperature, humidity, soil moisture, etc.)
- 🧠 ChatGPT API integration for dynamic decision-making and prompt programming
- 📷 Raspberry Pi-powered image capturing and cloud upload
- ⚙️ Automated actuator control: fans, lights, water pumps
- 📝 Configurable rule engine and system settings
- 📊 Data logging for analysis and optimization

---

## 🧩 Project Structure

```
greenhouse-gpt-automation/
├── hardware/               # Microcontroller and Pi code
├── software/               # AI/logic handling modules
├── configs/                # Environment and system config files
├── docs/                   # Architecture diagrams, flowcharts
├── data/                   # Sensor logs or sample datasets
├── requirements.txt        # Python dependencies
├── .gitignore
├── LICENSE
└── README.md
```

---

## ⚙️ Technologies Used

- **ESP32 / Raspberry Pi**
- **Python, C++ (Arduino)**
- **OpenAI ChatGPT API**
- **YAML / ENV for configurations**
- **GitHub for version control**

---

## 📦 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Ridmal97/greenhouse-gpt-automation.git
cd greenhouse-gpt-automation
```

### 2. Set up your environment

- Create your `.env` file based on `configs/credentials_example.env`
- Modify `system_config.yaml` with your hardware and API settings

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🛡️ License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Feel free to submit issues, fork the repo and create pull requests. Collaboration is welcome!

---

## 👨‍💻 Author

Developed by [Ridmal Kodikara](https://github.com/Ridmal97)
