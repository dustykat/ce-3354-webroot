
# 💧 Work It Out: Hydrology Problem Set

---

## 🧮 Work It Out: Reservoir Irrigation Planning

### Problem Statement
A farm has a reservoir with **vertical sides** and a **surface area of 2.5 acres**. At the start of the dry season, the reservoir contains **9.84 feet** of water depth.

During the dry season:
- The reservoir **loses 2.5 inches of water per week** due to **evaporation**.
- The **average irrigation demand** is **0.23 acre-feet per day**.

### Your Task:
**Determine how many full weeks** the farm can supply irrigation water from the reservoir before it is depleted.

### What You Know:

| Quantity                        | Value                    | Units         |
|--------------------------------|--------------------------|---------------|
| Reservoir surface area         | 2.5                      | acres         |
| Initial water depth            | 9.84                     | feet          |
| Evaporation loss rate          | 2.5                      | inches/week   |
| Irrigation demand              | 0.23                     | acre-ft/day   |

### Step 1: Compute Total Initial Volume in the Reservoir

$\text{Total Volume} = \text{Depth} \times \text{Surface Area}$

$\text{Total Volume} = 9.84 \, \text{ft} \times 2.5 \, \text{acres} = 24.6 \, \text{acre-ft}$

### Step 2: Convert Weekly Evaporation to Volume Loss

$2.5 \, \text{in} = \frac{2.5}{12} = 0.2083 \, \text{ft}$

$\text{Evaporation Volume per Week} = 0.2083 \, \text{ft} \times 2.5 \, \text{acres} = 0.5208 \, \text{acre-ft/week}$

### Step 3: Compute Weekly Irrigation Demand

$\text{Irrigation Volume per Week} = 0.23 \, \text{acre-ft/day} \times 7 = 1.61 \, \text{acre-ft/week}$

### Step 4: Compute Total Weekly Loss

$\text{Total Weekly Loss} = 0.5208 + 1.61 = 2.1308 \, \text{acre-ft/week}$

### Step 5: Compute Maximum Number of Weeks

$\text{Number of Weeks} = \frac{24.6}{2.1308} \approx 11.55$

### ✅ Final Answer:
**The farm can irrigate for approximately 11 full weeks.**

---

## 🧮 Work It Out: Estimating Streamflow from Precipitation

### Problem Statement
The **mean annual precipitation** for a **132 square-mile watershed** is **25 inches**.  
Assume that **20%** of the precipitation reaches the outlet as **streamflow**.

### Your Tasks:
- a) Acre-feet per year  
- b) Cubic feet per second (cfs)  
- c) Cubic meters per second (cms)

### What You Know:

| Quantity                        | Value                    | Units          |
|--------------------------------|--------------------------|----------------|
| Watershed area                 | 132                      | square miles   |
| Mean annual precipitation      | 25                       | inches/year    |
| Runoff coefficient             | 0.20                     | -              |

### Step 1: Convert Area

$132 \times 640 = 84,480 \, \text{acres}$

### Step 2: Convert Precipitation

$25 \, \text{in} = 2.0833 \, \text{ft}$

### Step 3: Total Volume

$84,480 \times 2.0833 = 175,919.184 \, \text{acre-ft/year}$

### Step 4: Streamflow Volume

$0.20 \times 175,919.184 = 35,183.837 \, \text{acre-ft/year}$

✅ **Answer (a):** 35,184 acre-ft/year

### Step 5: Convert to cfs

$\frac{35,183.837 \times 43,560}{31,536,000} \approx 48.6 \, \text{cfs}$

✅ **Answer (b):** 48.6 cfs

### Step 6: Convert to cms

$48.6 \times 0.0283168 = 1.377$

✅ **Answer (c):** 1.38 cms

---

## 🧮 Work It Out: Annual Rainfall Volume Over a Watershed

### Problem Statement
A **280 km² watershed** receives **725 mm** of rain annually.

### Your Tasks:
- a) Cubic meters  
- b) Cubic feet  
- c) Gallons  
- d) Acre-feet

### Step 1: Convert Units

Area: $280 \times 10^6 = 280,000,000 \, \text{m}^2$  
Rainfall: $725 \text{ mm} = 0.725 \, \text{m}$

### Step 2: Compute Volume

$0.725 \times 280,000,000 = 203,000,000 \, \text{m}^3$

✅ **Answer (a):** 203,000,000 m³

### Step 3: Convert to Other Units

- Cubic feet: $203,000,000 \times 35.3147 = 7.17 \times 10^9$
- Gallons: $203,000,000 \times 264.172 = 5.31 \times 10^{10}$
- Acre-feet: $\frac{203,000,000}{1233.48} = 164,541$

✅ **Answers:**
- (b) 7.17 × 10⁹ ft³  
- (c) 5.31 × 10¹⁰ gallons  
- (d) 164,541 acre-feet

---

## 🧮 Work It Out: Estimating Annual Evaporation Using Water Budget

### Problem Statement
A **600-hectare** farm receives **2500 mm** of rainfall annually.  
A river **enters at 5 m³/s** and **exits at 4 m³/s**.  
**Storage increases by 2.5 × 10⁶ m³** annually.

### Your Task:
Estimate **annual evaporation** in **mm** using the **water budget**.

### Step 1: Convert Area and Rainfall

$600 \times 10,000 = 6,000,000 \, \text{m}^2$  
$2500 \, \text{mm} = 2.5 \, \text{m}$

Rainfall volume = $2.5 \times 6,000,000 = 15,000,000 \, \text{m}^3$

### Step 2: River Inflow – Outflow (Net)

Net inflow = $1 \, \text{m}^3/s$  
Annual = $1 \times 31,536,000 = 31,536,000 \, \text{m}^3$

### Step 3: Apply Water Budget

Evaporation = $(15,000,000 + 31,536,000) - 2,500,000 = 44,036,000 \, \text{m}^3$

### Step 4: Convert to Depth

$\frac{44,036,000}{6,000,000} = 7.339 \, \text{m} = 7339 \, \text{mm}$

### ✅ Final Answer:
**7339 mm of evaporation per year**

---
