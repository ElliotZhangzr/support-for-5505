# Checkpoint2 会议准备文档

## 1. 构建的应用（Application Decision）

**股票模拟交易平台（Stock Trading Simulation Platform）**

应用目标：
- 用户注册/登录后，获得初始虚拟资金并开始交易。
- 用户可查看实时行情与历史走势，进行买入/卖出。
- 用户可查看持仓、账户余额、总资产与盈亏表现。
- 系统提供排行榜，支持用户之间的表现比较。
- 管理员可管理股票参数与用户角色，保证系统可演示、可运营。（待定）


---

## 2. 网站主要页面列表（Main Pages List）


### 2.1 认证与账户初始化

1. **注册页面**（/register）
- 作用：新用户创建账户。
- 对应 user stories：
  - #2 Account Registration and Login

2. **登录页面**（/login）
- 作用：用户登录系统，首次登录后可使用初始虚拟资金。
- 对应 user stories：
  - #1 Initial Virtual Funds
  - #2 Account Registration and Login

### 2.2 核心交易与资产查看

3. **Dashboard 主页面**（/dashboard）
- 作用：系统核心页面，包含：
  - 账户现金、总资产
  - 股票价格与历史图表
  - 买入/卖出交易入口
  - 持仓列表与盈亏展示
  - 市场概览
- 对应 user stories：
  - #3 Account Balance and Profit/Loss
  - #4 Portfolio Viewing
  - #5 Real-Time Stock Prices
  - #6 Historical Price Trends
  - #7 Buy Stocks
  - #8 Sell Stocks
  - #9 Transaction Feedback

4. **用户列表页面**（/users）
- 作用：展示社区用户基础信息（用户名、邮箱、注册时间）。
- 对应 user stories：
  - 社区可见性辅助页面（不直接对应核心交易故事，但支持系统完整性展示）

5. **排行榜页面**（/leaderboard）
- 作用：展示总资产榜和现金榜，支持用户比较表现。
- 对应 user stories：
  - #10 Leaderboard

### 2.3 系统管理页面（管理员）

6. **管理员主页**（/admin）
- 作用：平台 KPI、用户角色管理、股票管理、参数预设中心。
- 对应 user stories：
  - 系统运营支撑页面（保障交易系统可管理、可维护）

7. **管理员股票详情页面**（/admin/stocks/<symbol>）（待定）
- 作用：单只股票参数精细化调整、future override、重置与删除等生命周期操作。
- 对应 user stories：
  - 系统运营支撑页面（用于保证市场行为可控与可演示）

---

## 3. CSS 框架决策（CSS Framework）

**Bootstrap 5.3.3**

### 3.1 决策依据

1. Bootstrap 可快速保证响应式布局，满足课程项目在有限时间内稳定交付的需求。

### 3.2 实施方式

- 保持 Bootstrap 作为基础 UI 框架（布局、表单、按钮、表格、卡片、导航、Toast）。
- 在 static/styles.css 中叠加项目自定义样式，形成统一视觉风格（背景渐变、卡片阴影、交易页与后台页细节风格）。

