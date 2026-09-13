# OceanEmbed Frontend

React + Vite frontend for the OceanEmbed subsurface temperature
reconstruction MVP. Talks to the FastAPI backend's `/predict` and
`/ocean-data` endpoints.

## Run locally

Start the backend first (from `ocean-backend/`, e.g. `docker-compose up`
or `uvicorn app.main:app --reload`), then:

```bash
npm install
npm run dev
```

Opens at `http://localhost:5173`. It expects the backend at
`http://localhost:8000` by default. To point at a different backend URL,
create a `.env` file here:

```
VITE_API_BASE=http://your-backend-host:8000
```

## What it does

1. **Location & date** — pick a date and lat/lon inside the model's domain
   (5°N–30°N, 45°E–105°E). "Fetch stored surface data" calls
   `GET /ocean-data` to prefill SST/SSS/SSH/currents if a row exists for
   that date and grid cell; otherwise you enter values manually.
2. **Reconstruct** — `POST /predict` sends the 5 surface inputs to the
   model and gets back `depths` (15 standard levels) and a full
   `temperature` grid.
3. **Results** — the app reads the single grid cell nearest the requested
   lat/lon out of that grid (see `extractProfile` in `src/api.js`) and
   shows it as a vertical water-column visual, a depth-vs-temperature
   line chart, and a table.

## Known limitations (matches current backend)

- The backend model currently takes **5 inputs only** — wind is not yet
  wired in, even though it's part of the longer-term plan. The footer
  note in the UI reflects this; update it if/when the backend adds wind.
- `/predict` returns a full 100×240 grid per depth level even though the
  request is for a single point (the current backend expands the point
  input uniformly across the grid before running the model). The frontend
  only reads one cell out of it. This is fine for an MVP but is worth
  changing backend-side later — either return just the requested cell, or
  make `/predict` genuinely spatial by accepting a full input grid.
- Values away from the domain edges will look nearly identical for
  different lat/lon at the *same* date/surface inputs, since the model
  input is currently the same value broadcast across the whole grid —
  this is a backend/model behavior, not a frontend bug.

## Project structure

```
src/
  api.js                 API client + grid helpers
  App.jsx                page state and layout
  styles.css              design tokens and styles
  components/
    QueryPanel.jsx        location/date/surface parameter form
    WaterColumn.jsx        hero depth-profile visual
    ProfileChart.jsx       depth vs temperature line chart
    ProfileTable.jsx       raw values table
```
