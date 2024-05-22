# AD22_DLP_Project1_Aebli_Senn
Repository for the Project work 1 of the Digital Labs and Production track of the Applied Digital Life Sciences (ADLS) program at ZHAW
The relevant code and the environment relevant for this project can be found in the folder "PA1_DavidSenn_KaiAebli"
## Process Modeling and Implementation with Python, Node-RED and Raspberry Pi

**Zusammenfassung**
Dieses Projekt untersucht die Integration von Raspberry Pi (RPi) mit Dobot Magician Roboterar-men zur Prozessautomatisierung in einer Internet of Things (IoT) Umgebung unter Verwendung von Python und Node-RED. Das Ziel ist es, die Machbarkeit und die Vorteile der Kombination dieser Technologien zur Automatisierung eines Sortierprozesses zu demonstrieren. Das Projekt konzentriert sich auf drei Hauptbereiche: die Anwendung von RPi als Edge-Computing-Geräte, die Nutzbarkeit von Node-RED als No-Code-Entwicklungsumgebung und die effektive Steuerung der Dobot Magician Roboter durch Python-Skripte.
Das Hardware-Setup umfasst drei RPis und drei Dobot Magician Roboter, die mit einem Förder-band, einer Lichtschranke und einem Farbsensor ausgestattet sind. Node-RED orchestriert die Kommunikation und den Prozessablaufs, wobei die Prozess- und Nachrichtenflüsse in vereinfach-ter und standardisierter Weise mit der Business Process Model and Notation (BPMN) visualisiert werden. Python-Skripte steuerten die Roboter und Peripheriegeräte.
Das implementierte System automatisiert erfolgreich den Transport und die anschliessende Sor-tierung von roten, grünen und blauen Blöcken entsprechend ihrer Farbe und demonstriert die Fä-higkeit der RPis, Prozesssteuerung und Kommunikation effizient zu handhaben. Node-RED bietet eine intuitive Schnittstelle für das Prozessmanagement und vereinfacht die Entwicklung des Edge-Cloud-Systems für Kommunikationsflüsse zwischen den verschiedenen RPis.
Das Projekt bestätigt, dass die Integration von RPi und Dobot Magician Robotern deren Funktio-nalität verbessert und sie in effiziente IoT-Geräte verwandelt, die in der Lage sind, komplexe Auf-gaben auszuführen. Die benutzerfreundliche Umgebung von Node-RED erweist sich als effektiv für das Management des Automatisierungsprozesses, während die Flexibilität von Python eine robuste Steuerung des Robotersystems gewährleistet. Trotz Herausforderungen bei der Doku-mentation der verfügbaren Python-Bibliotheken und Sensorbeschränkungen hebt das Projekt das Potenzial dieser Technologien in der industriellen Automatisierung hervor und bietet Einblicke in zukünftige Verbesserungen, wie fortschrittliche Farberkennung und verbesserte Dokumentation.

**Abstract**
This project explores the integration of Raspberry Pi (RPi) with Dobot Magician robotic arms for process automation in an Internet of Things (IoT) environment, employing Python and Node-RED. The objective is to demonstrate the feasibility and benefits of combining these technologies to automate a sorting process. The project focuses on three key areas: the application of RPi as edge computing devices, the usability of Node-RED as a no-code development environment, and the effective control of Dobot Magician robots through Python scripting.
The hardware setup involves three RPis and three Dobot Magician robots equipped with a con-veyor belt, a photoelectric barrier, and a color sensor. Node-RED orchestrates the communication and process flow, with Business Process Model and Notation (BPMN) used to visualize these flows in a simplified and standardized manner. Python scripts control the robots and peripherals.
The implemented system successfully automates the transportation and subsequent sorting of red, green and blue blocks according to their color, demonstrating the RPIs ability to handle pro-cess control and communication efficiently. Node-RED provides an intuitive interface for process management and simplifies the development of the edge cloud for communication flows between the different RPis.
The project confirms that integrating RPi and Dobot Magician robots enhances their functionality and transforms them into efficient IoT devices capable of performing complex tasks. Node-RED's user-friendly environment proves effective for managing the automation process, while Python's flexibility ensures robust control of the robotic system. Despite challenges with the documentation of the available Python libraries and sensor limitations, the project highlights the potential of these technologies in industrial automation and offers insights for future enhancements, such as ad-vanced color detection and improved documentation.




## Initialer Projektauftrag:
**Beschreibung:**

Roboterarme und andere Aktuatoren spielen eine grosse Rolle in der Automatisierung von Prozessen in Labors und Produktionsanlagen. Beispiele für solche Geräte stehen im Departement in Form von Dobot Magicians bereit. Der Dobot Magician ist ein 4-Achs-Roboterarm, der sich für verschiedene Aufgaben im Laborkontext eignen. Solche Roboterarme und andere Aktuatoren arbeiten oft in strikt definierten Prozessen zusammen, wobei der Prozessablauf je nach Kontext auf gewisse äussere Signale oder Gegebenheiten Rücksicht nimmt. Die semi-formale Modellierung solcher Prozesse spielt in der Digitalisierung und Automatisierung von Laboren und Produktionsanlagen eine wichtige Rolle. 
Die Roboterarme lassen sich über die sog. "No-Code"-Umgebungen Node-Red und Blockly programmieren. In einer "No-Code"-Umgebungen werden Funktionale Blöcke in einer grafischen Oberfläche arrangiert.

**Auftrag:**

Das Projekt analysiert verschiedene Ansätze zur "No-Code"-Programmierung für die Dobot-Roboter in der Anwendung. Das Projekt untersucht Ähnlichkeiten und Unterschiede der verschiedenen Ansätze und wie die verschiedenen Konzepte zwischen den Ansätzen übersetzt werden. 
1.	**Literaturrecherche:** Recherchieren Sie geeignete Literaturquellen zum Thema Prozessmodellierung mit Blockly und Node-RED. Beschreiben Sie die wesentlichen Erkenntnisse und Methoden, die in der Literatur vorgestellt werden.
2.	**Manuelle Implementierung:** Skizzieren Sie den Prozessablauf von Hand, um ein grundlegendes Verständnis des Prozesses zu erlangen.
3.	**Erstellung eines Prozessfliessbildes:** Verwenden Sie BPMN (Business Process Model and Notation), um ein detailliertes Prozessfliessbild des skizzierten Ablaufs zu erstellen.
4.	**Abstraktion und Parametrisierung:** Analysieren Sie den erstellten Prozess, identifizieren Sie wiederkehrende Muster und abstrahieren Sie diese. Parametrieren Sie den Prozess entsprechend, um Flexibilität und Wiederverwendbarkeit zu gewährleisten.
5.	**Implementierung mit Blockly und Python:** Nutzen Sie das Blockly-Tool der Dobots, um den Prozess unter Verwendung von Python zu implementieren.
6.	**Ausführung mit Node-RED:** Integrieren Sie den mit Blockly erstellten Prozess in Node-RED und führen Sie diesen aus. Dokumentieren Sie alle erforderlichen Schritte und beachten Sie mögliche Integrationsprobleme.

**Resultate:**

* Erstellen Sie einen Report, in dem Sie den gesamten Entwicklungsprozess und die daraus gewonnenen Erkenntnisse sowie die implementierten Lösungen dokumentieren. Berücksichtigen Sie dabei auch mögliche Herausforderungen und Problemlösungsstrategien.


**Abgrenzung:**

* Prozessablauf nicht von aussen steuerbar.
* Keine Verwendung weiterer Sensordaten.

**Voraussetzungen:**

* Abstraktion von physischen Abläufen
* Physical Computing
* Softwareentwicklung mit Python

**Kompetenzgewinn:**

* Praktische Fähigkeiten in Prozessmodellierung.
* Abstraktion und Parametrisierung.
* Integration in Node-RED.
* Kritisches Denken und Problemlösungsfähigkeiten.

## Process Modeling and Implementation with Blockly, Python, and Node-RED

**Description:**

Robot arms and other actuators play an important role in the automation of processes in laboratories and production plants. Examples of such devices are available in the department in the form of Dobot Magicians. The Dobot Magician is a 4-axis robot arm that is suitable for various tasks in the laboratory context. Such robot arms and other actuators often work together in strictly defined processes, whereby the process flow takes into account certain external signals or conditions depending on the context. The semi-formal modeling of such processes plays an important role in the digitization and automation of laboratories and production plants. The robot arms can be programmed using the so-called "no-code" environments Node-Red and Blockly. In a "no-code" environment, functional blocks are arranged in a graphical interface.

**Tasks:**

1. **Literature Review:** Conduct research on process modeling with Blockly and Node-RED.
2. **Manual Implementation:** Sketch the process flow to gain a basic understanding.
3. **Process Flowchart:** Create a detailed process flowchart using BPMN (Business Process Model and Notation).
4. **Abstraction and Parameterization:** Analyze the process, identify recurring patterns, and abstract them. Parameterize the process for flexibility and reusability.
5. **Implementation with Blockly and Python:** Utilize the Dobot's Blockly tool to implement the process using Python.
6. **Execution with Node-RED:** Integrate the Blockly-created process into Node-RED and execute it. Document all necessary steps and consider potential integration issues.

**Results:**

* Create a report documenting the entire development process, gained insights, and implemented solutions.
* Include encountered challenges and problem-solving strategies.

**Delimitations:**

* The process flow will not be externally controllable.
* No additional sensor data will be used for control.

**Prerequisites:**

* Abstraction of physical processes
* Physical Computing
* Software development with Python

**Learning Outcomes:**

* Students will gain practical skills in process modeling through manual implementation and flowchart creation.
* The abstraction and parameterization phase teaches students to look beyond the specific context of a single process and identify generalizable patterns.
* Integration with Node-RED, along with its associated documentation and troubleshooting, prepares students for challenges encountered in real-world projects, fostering critical thinking and problem-solving skills.
