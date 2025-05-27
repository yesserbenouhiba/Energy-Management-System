# Energy Management System

A comprehensive web application for managing energy-related data including companies, accounts, electricity/gas meters, quotation requests, and professional sales. Built with Django REST Framework backend and Vue.js frontend.

## 📋 Implemented Features

### Backend Features (Django REST API)
- **Authentication System**: Token-based authentication with Django REST Framework
- **Company Management**: CRUD operations for energy companies with complete business information
- **Account Management**: User account creation and management with role-based access
- **Meter Management**: 
  - Electricity meter tracking with tariff options and power ratings
  - Gas meter monitoring with consumption data
- **Quotation System**: Request and manage energy quotations with status tracking
- **Professional Sales**: Complete sales lifecycle management with supplier integration
- **Statistics & Analytics**: Custom SQL queries for business intelligence
  - Quotation statistics and trends
  - Sales performance metrics  
  - Average duration calculations for business processes
- **RESTful API**: Full CRUD operations with proper HTTP methods and status codes
- **Data Validation**: Comprehensive input validation and error handling

### Frontend Features (Vue.js)
- **Modern Vue.js Application**: Built with Vite for optimal development experience
- **Component-Based Architecture**: Reusable components for scalable development
- **State Management**: Centralized state management with Vuex/Pinia
- **Routing**: Client-side routing for single-page application experience
- **API Integration**: Axios-based HTTP client for seamless backend communication
- **Responsive Design**: Mobile-friendly interface design

### Infrastructure
- **Docker Support**: Complete containerization for easy deployment
- **Environment Configuration**: Separate development and production configurations
- **Database Integration**: SQLite for development, easily configurable for production databases

## 🏗️ Design Decisions

### Backend Architecture
- **Django REST Framework**: Chosen for its robust serialization, authentication, and API documentation capabilities
- **Token Authentication**: Simple yet secure authentication suitable for API consumption
- **Model Relationships**: Properly structured foreign key relationships to maintain data integrity
- **Serializers**: Custom serializers for data validation and API response formatting
- **Modular Design**: Separated concerns with dedicated apps for different functionalities

### Frontend Architecture
- **Vue.js 3**: Selected for its reactive nature and excellent developer experience
- **Vite Build Tool**: Modern build tool for faster development and optimized production builds
- **Component Structure**: Organized components by feature for better maintainability
- **State Management**: Centralized state for consistent data flow across components

### Database Design
- **Normalized Structure**: Proper database normalization to avoid data redundancy
- **Foreign Key Constraints**: Maintains referential integrity across related entities
- **Flexible Schema**: Designed to accommodate future feature expansions

## 🚀 Setup Instructions

### Prerequisites
- Python 3.8+
- Node.js 14+
- npm
- Git
- Docker & Docker Compose (for containerized setup)

### Backend Setup (Django API)

1. **Navigate to the backend directory**
   ```bash
   cd energy_api
   ```

2. **Create and activate virtual environment**
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser account**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://127.0.0.1:8000/`

### Frontend Setup (Vue.js)

1. **Navigate to the frontend directory**
   ```bash
   cd energy-frontend
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Run the development server**
   ```bash
   npm run dev
   ```

The Vue application will be available at `http://localhost:5173` (or the port specified in your configuration).

### Docker Setup (Recommended for Production)

1. **Navigate to the main repository folder**
   ```bash
   cd Energy-Management-System
   ```

2. **Build the Docker containers**
   ```bash
   docker-compose build
   ```

3. **Start the application stack**
   ```bash
   docker-compose up
   ```

   To run in detached mode:
   ```bash
   docker-compose up -d
   ```

4. **Stop the application stack**
   ```bash
   docker-compose down
   ```

The Docker setup will start both the backend API and frontend application with all necessary dependencies.

## 🔐 Authentication

### Getting Started with API Authentication

1. **Get Authentication Token**
   - **Endpoint:** `POST /api-token-auth/`
   - **Request Body:**
   ```json
   {
       "username": "your_superuser_username",
       "password": "your_superuser_password"
   }
   ```
   - **Response:**
   ```json
   {
       "token": "32d06b5906fd53879540350565a921752d8fbc8f"
   }
   ```

2. **Use Token in API Requests**
   Add the following header to all API requests:
   ```
   Authorization: Token 32d06b5906fd53879540350565a921752d8fbc8f
   ```

## 📋 API Endpoints & Testing Data

### 1. Companies (Sociétés)
**Endpoint:** `POST /api/societes/`
```json
{
  "nom": "EnergieTech",
  "siret": "12345678901234",
  "siren": "123456789",
  "adressePostal": "12 Rue de l'Énergie",
  "codePostal": "75001",
  "commune": "Paris",
  "email": "contact@energietech.fr",
  "telephone": "+33123456789"
}
```

### 2. Accounts (Comptes)
**Endpoint:** `POST /api/comptes/`
```json
{
  "type": "Commercial",
  "email": "yasser@gmail.com",
  "nom": "Benouhiba",
  "prenom": "Yasser"
}
```

### 3. Electricity Meters (Compteurs Électriques)
**Endpoint:** `POST /api/compteurs-elec/`
```json
{
  "numCompteur": "ELEC123456",
  "adresseCompteur": "12 Rue Volt",
  "optionTarifaire": "Base",
  "puissance": 9,
  "societe": 1
}
```

### 4. Gas Meters (Compteurs Gaz)
**Endpoint:** `POST /api/compteurs-gaz/`
```json
{
  "numCompteur": "GAZ789456",
  "adresseCompteur": "14 Rue du Gaz",
  "consommation": 1500.50,
  "societe": 1
}
```

### 5. Quotation Requests (Demandes de Cotation)
**Endpoint:** `POST /api/demandes-cotation/`
```json
{
  "type": "GAZ",
  "societe": 1,
  "compte": 1,
  "numCompteur": "GAZ789456",
  "status": "Pending"
}
```

### 6. Professional Sales (Ventes Professionnelles)
**Endpoint:** `POST /api/ventepro/`
```json
{
  "societe": 1,
  "fournisseur": "TotalEnergies",
  "numCompteur": "ELEC123456",
  "dateDebutFourniture": "2025-06-01",
  "dateFinFourniture": "2026-06-01",
  "status": "Pending"
}
```

## 📊 SQL Queries & Statistics (Bonus Features)

The system includes advanced statistical endpoints that utilize custom SQL queries for business intelligence:

### Available Statistics Endpoints
- **Dashboard Metrics:** `GET /api/dashboard-metrics/`
  - Shows key metrics including active contracts and pending quotations
- **Quotation Requests with Details:** `GET /api/quotation-requests-details/`
  - Lists all quotation requests with complete company and account information
- **Sales Statistics:** `GET /api/sales-statistics/`
  - Provides sales data grouped by energy type and company
- **Average Contract Duration:** `GET /api/average-contract-duration/`
  - Calculates average contract duration by supplier

### Implemented SQL Queries

#### 1. Quotation Requests with Company and Account Details
```sql
SELECT 
    dc.id,
    dc.type,
    dc.status,
    dc.numCompteur,
    s.nom AS company_name,
    s.siret,
    s.siren,
    s.email AS company_email,
    c.nom AS account_lastname,
    c.prenom AS account_firstname,
    c.email AS account_email,
    c.type AS account_type
FROM 
    core_demandecotation dc
JOIN 
    core_societe s ON dc.societe_id = s.id
JOIN 
    core_compte c ON dc.compte_id = c.id;
```

#### 2. Sales Statistics Grouped by Energy Type and Company
```sql
SELECT 
    s.nom AS company_name,
    vp.fournisseur,
    COUNT(*) AS total_sales,
    CASE 
        WHEN vp.numCompteur IN (SELECT numCompteur FROM core_compteurelec) THEN 'ELEC'
        WHEN vp.numCompteur IN (SELECT numCompteur FROM core_compteurgaz) THEN 'GAZ'
        ELSE 'UNKNOWN'
    END AS energy_type
FROM 
    core_ventepro vp
JOIN 
    core_societe s ON vp.societe_id = s.id
GROUP BY 
    s.nom, vp.fournisseur, energy_type;
```

#### 3. Average Contract Duration by Supplier
```sql
SELECT 
    fournisseur,
    AVG(JULIANDAY(dateFinFourniture) - JULIANDAY(dateDebutFourniture)) AS average_duration_days
FROM 
    core_ventepro
WHERE 
    status = 'Active'
GROUP BY 
    fournisseur;
```

### SQL Query Features
- **Complex Joins**: Multi-table joins to combine related data from companies, accounts, and quotations
- **Conditional Logic**: CASE statements to categorize energy types based on meter numbers
- **Aggregation Functions**: COUNT() and AVG() for statistical calculations
- **Date Calculations**: JULIANDAY() function for calculating duration between dates
- **Data Filtering**: WHERE clauses for filtering active contracts and specific statuses

## ⚠️ Known Limitations & Areas for Improvement

### Current Limitations

1. **Authentication System**
   - Currently uses simple token authentication
   - No token expiration mechanism implemented
   - Limited role-based access control
   - Tokens are not stored securely – currently not stored in HTTP-only cookies, leaving them vulnerable to XSS attacks
   - Frontend routes are not protected – users can access pages without authentication

2. **Database**
   - SQLite used for development (not suitable for production scale)

3. **Error Handling**
   - Basic error responses implemented
   - Could benefit from more detailed error codes and messages

4. **Testing**
   - Unit tests not implemented
   - No integration tests for API endpoints

### Areas for Improvement

1. **Security Enhancements**
   - Implement JWT tokens with expiration
   - Store tokens in HTTP-only cookies to protect against XSS attacks
   - Protect frontend routes based on authentication status

2. **Feature Enhancements**
   - Advanced reporting and dashboard features
   - File upload functionality for documents
   - Email integration for notifications
   - Multi-language support

3. **DevOps & Deployment**
   - CI/CD pipeline setup

## 📁 Project Structure

### Main Repository Structure
```
Energy-Management-System/
├── energy_api/                 # Django Backend API
├── energy-frontend/            # Vue.js Frontend Application
├── docker-compose.yml          # Docker Compose configuration
└── README.md                   # Main project documentation
```

### Backend Structure (energy_api/)
```
energy_api/
├── core/
│   ├── __pycache__/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── energy_api/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── venv/
├── .gitignore
├── db.sqlite3
├── Dockerfile
├── manage.py
└── requirements.txt
```

### Frontend Structure (energy-frontend/)
```
ENERGY-FRONTEND/
├── .vscode/
├── node_modules/
├── public/
├── src/
│   ├── assets/
│   ├── components/
│   ├── pages/
│   ├── router/
│   ├── store/
│   ├── App.vue
│   ├── axios.js
│   ├── main.js
│   └── style.css
├── .env
├── .gitignore
├── Dockerfile
├── index.html
├── nginx.conf
├── package-lock.json
├── package.json
├── README.md
└── vite.config.js
```
