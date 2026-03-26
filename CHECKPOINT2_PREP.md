正在优化工具选择...# Checkpoint 2 Meeting Preparation Document

## 1. Application Decision

**Stock Trading Simulation Platform**

Application goals:
- After users register/log in, they receive initial virtual funds and can start trading.
- Users can view real-time quotes and historical trends, and place buy/sell orders.
- Users can view holdings, cash balance, total assets, and profit/loss performance.
- The system provides a leaderboard to support performance comparison among users.
- Admins can manage stock parameters and user roles to ensure the system is demo-ready and operable. (TBD)

---

## 2. Main Website Pages List

### 2.1 Authentication and Account Initialization

1. **Registration Page** (/register)
- Purpose: Create a new user account.
- Related user stories:
  - #2 Account Registration and Login

2. **Login Page** (/login)
- Purpose: Log in to the system; users can access initial virtual funds after first login.
- Related user stories:
  - #1 Initial Virtual Funds
  - #2 Account Registration and Login

### 2.2 Core Trading and Asset Overview

3. **Dashboard Main Page** (/dashboard)
- Purpose: Core system page, including:
  - Account cash and total assets
  - Stock prices and historical charts
  - Buy/sell trading entry
  - Holdings list and profit/loss display
  - Market overview
- Related user stories:
  - #3 Account Balance and Profit/Loss
  - #4 Portfolio Viewing
  - #5 Real-Time Stock Prices
  - #6 Historical Price Trends
  - #7 Buy Stocks
  - #8 Sell Stocks
  - #9 Transaction Feedback

4. **Users Page** (/users)
- Purpose: Display basic community user information (username, email, registration date).
- Related user stories:
  - Community visibility support page (does not directly map to core trading stories, but supports completeness of system demonstration)

5. **Leaderboard Page** (/leaderboard)
- Purpose: Display total-asset ranking and cash ranking for user performance comparison.
- Related user stories:
  - #10 Leaderboard

### 2.3 System Management Pages (Admin)

6. **Admin Home Page** (/admin)
- Purpose: Platform KPI dashboard, user role management, stock management, and parameter preset center.
- Related user stories:
  - System operation support page (ensures the trading platform is manageable and maintainable)

7. **Admin Stock Detail Page** (/admin/stocks/<symbol>) (TBD)
- Purpose: Fine-grained parameter tuning for individual stocks, future overrides, reset/delete lifecycle operations, etc.
- Related user stories:
  - System operation support page (used to keep market behavior controllable and demo-ready)

---

## 3. CSS Framework Decision

**Bootstrap 5.3.3**

### 3.1 Rationale

1. Bootstrap enables rapid responsive layout implementation, meeting the course project’s need for stable delivery within limited time.

### 3.2 Implementation Approach

- Keep Bootstrap as the base UI framework (layout, forms, buttons, tables, cards, navigation, toasts).
- Layer project-specific styles in static/styles.css to build a unified visual style (gradient background, card shadows, and detailed styles for trading pages and admin pages).