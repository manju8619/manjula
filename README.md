# 🚍 Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit

## 🧠 Skills You'll Gain
- Web Scraping with Selenium
- Python Programming
- Interactive Dashboards using Streamlit
- SQL Database Integration
- Data Filtering and Analysis

---

## 🌐 Domain
**Transportation**

---

## 📌 Problem Statement

This project focuses on automating the extraction of detailed bus travel information from [Redbus.in](https://www.redbus.in/) using **Selenium**, and making it interactive via **Streamlit**. The goal is to:
- Streamline travel data collection (routes, prices, availability, etc.)
- Provide interactive filtering for users through a user-friendly dashboard
- Enhance strategic decision-making and customer services in the transportation industry

---

## 💼 Business Use Cases

- **Travel Aggregators:** Provide real-time bus info (schedules, seat availability).
- **Market Analysis:** Understand travel patterns for better planning.
- **Customer Service:** Offer personalized trip options.
- **Competitor Analysis:** Compare pricing and services with competitors.

---

## 🚀 Approach

### 🔎 Data Scraping
- Selenium is used to automate browsing and data extraction from the Redbus website.
- Information extracted includes:
  - Bus routes and links
  - Bus names
  - Bus types (Sleeper/Seater/AC/Non-AC)
  - Departure/arrival times
  - Ratings, prices, and seat availability

### 🗄️ Data Storage
- Scraped data is stored in an SQL database using a custom schema (see below).

### 💻 Streamlit Application
- A user-friendly Streamlit dashboard allows:
  - Data filtering by route, bus type, price range, star rating, and availability
  - SQL-based querying to handle dynamic user input

---

## 🧱 Database Schema

**Table: `bus_routes`**

| Column Name      | Data Type | Description                                  |
|------------------|-----------|----------------------------------------------|
| `id`             | INT       | Primary Key (Auto-increment)                 |
| `route_name`     | TEXT      | Route information (From → To)                |
| `route_link`     | TEXT      | Link to Redbus route page                    |
| `busname`        | TEXT      | Bus or operator name                         |
| `bustype`        | TEXT      | Type (Sleeper, Seater, AC, Non-AC)           |
| `departing_time` | TIME      | Departure time                               |
| `duration`       | TEXT      | Journey duration                             |
| `reaching_time`  | TIME      | Arrival time                                 |
| `star_rating`    | FLOAT     | Passenger rating                             |
| `price`          | DECIMAL   | Ticket price                                 |
| `seats_available`| INT       | Number of seats available                    |

---

## 📊 Results & Objectives

✅ Scrape **10+ Government State Transport** and private bus data  
✅ Store structured data in an SQL database  
✅ Create an interactive **Streamlit app** for dynamic filtering  
✅ Deliver an intuitive and efficient UI  

---

## 📈 Project Evaluation Metrics

- **Scraping Accuracy**: Correctness of scraped data
- **Database Design**: Efficiency of schema and queries
- **App Usability**: Ease of navigation and interaction
- **Filter Functionality**: Effectiveness of dynamic filters
- **Code Quality**: Follows best practices and PEP 8

---

## 🛠️ Tech Stack

- Python  
- Selenium  
- SQL (SQLite / MySQL / PostgreSQL)  
- Streamlit  
- Git & GitHub  

---

## 📁 Project Structure

```bash
redbus-scraper/
│
├── scraping/
│   └── redbus_scraper.py        # Selenium scraper script
│
├── database/
│   ├── schema.sql               # SQL schema for bus_routes table
│   └── insert_data.py           # Script to populate database
│
├── streamlit_app/
│   └── app.py                   # Streamlit UI and filtering logic
│
├── utils/
│   └── db_helper.py             # Database connection and queries
│
├── README.md
└── requirements.txt
