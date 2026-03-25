# Project Guide (Team Edition)

## 1. Project Overview

This is a Flask-based stock trading simulation system. Its core features include:

- User registration, login, and logout
- User holdings and cash management
- Market price simulation with automatic updates
- Buy/sell trading operations
- Leaderboard
- Admin panel (stock parameters, reset, delete, presets, user roles)

The current main backend file is `app.py`, and the market simulation logic is provided by `stock_engine.py`.

## 2. Environment Setup in VS Code

Python 3.11+ is recommended.

1. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

## 3. Startup Commands

Start in development mode:

```bash
python app.py
```

## 4. Directory and Key Files

- `app.py`: Main backend, including models, routes, authentication, trading, and admin features
- `stock_engine.py`: Price simulation engine
- `templates/`: Page templates
- `static/`: Styles and static assets
- `app.db`: SQLite database file (generated after running)

## 5. Main Business Flow

1. User registers and logs in
2. User enters Dashboard to view price curves and market information
3. User places buy/sell orders (`/api/trade`)
4. System updates holdings and cash (`/api/portfolio`)
5. Leaderboard ranks users by total assets/cash (`/leaderboard`)
6. Admin can adjust stock parameters and user roles in the admin panel

## 6. Permission Rules

- Not logged in: Can only access `login/register`; protected pages redirect to login
- Logged in: Can access `dashboard/users/leaderboard` and user-related APIs
- Admin: Can access all `/admin` pages and admin APIs

