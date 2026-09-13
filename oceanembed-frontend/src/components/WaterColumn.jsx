import { useMemo } from "react";

// Colour ramp from warm surface to cold deep water. Interpolated in a
// few fixed steps rather than a formula, so the palette can be tuned
// by eye without touching the layout math below.
const RAMP = [
  { t: 30, color: "#FF8659" }, // warm surface
  { t: 24, color: "#F2B15C" },
  { t: 18, color: "#7FD1C8" },
  { t: 10, color: "#4CC9D6" },
  { t: 4, color: "#2E7FA8" },
  { t: 0, color: "#173B5E" }, // cold deep water
];

function colorForTemp(temp) {
  if (temp >= RAMP[0].t) return RAMP[0].color;
  if (temp <= RAMP[RAMP.length - 1].t) return RAMP[RAMP.length - 1].color;

  for (let i = 0; i < RAMP.length - 1; i++) {
    const hi = RAMP[i];
    const lo = RAMP[i + 1];
    if (temp <= hi.t && temp >= lo.t) {
      const span = hi.t - lo.t || 1;
      const f = (temp - lo.t) / span;
      return mix(lo.color, hi.color, f);
    }
  }
  return RAMP[RAMP.length - 1].color;
}

function mix(hexA, hexB, f) {
  const a = hexToRgb(hexA);
  const b = hexToRgb(hexB);
  const r = Math.round(a.r + (b.r - a.r) * f);
  const g = Math.round(a.g + (b.g - a.g) * f);
  const bl = Math.round(a.b + (b.b - a.b) * f);
  return `rgb(${r}, ${g}, ${bl})`;
}

function hexToRgb(hex) {
  const n = parseInt(hex.slice(1), 16);
  return { r: (n >> 16) & 255, g: (n >> 8) & 255, b: n & 255 };
}

// Depth is placed on a sqrt scale so the dynamic near-surface layers
// (0–200m) get proportionally more vertical room than the slow-changing
// deep layers, without depths below 1000m ever needing to be shown.
function depthToY(depth, maxDepth, height) {
  return (Math.sqrt(depth) / Math.sqrt(maxDepth)) * height;
}

export default function WaterColumn({ depths, temperatures }) {
  const width = 340;
  const height = 420;
  const padTop = 28;
  const padBottom = 16;
  const trackH = height - padTop - padBottom;
  const maxDepth = depths[depths.length - 1];

  const stops = useMemo(() => {
    return depths.map((d, i) => ({
      depth: d,
      temp: temperatures[i],
      y: padTop + depthToY(d, maxDepth, trackH),
      color: colorForTemp(temperatures[i]),
    }));
  }, [depths, temperatures, maxDepth, trackH]);

  const gradientId = "water-column-gradient";

  return (
    <div className="water-column">
      <svg
        viewBox={`0 0 ${width} ${height}`}
        role="img"
        aria-label="Reconstructed temperature by depth, from surface to 1000 metres"
      >
        <defs>
          <linearGradient id={gradientId} x1="0" y1="0" x2="0" y2="1">
            {stops.map((s, i) => (
              <stop
                key={i}
                offset={`${(s.y - padTop) / trackH * 100}%`}
                stopColor={s.color}
              />
            ))}
          </linearGradient>
        </defs>

        <rect
          x={70}
          y={padTop}
          width={64}
          height={trackH}
          rx={10}
          fill={`url(#${gradientId})`}
        />

        {stops.map((s, i) => (
          <g key={i}>
            <line
              x1={70}
              y1={s.y}
              x2={134}
              y2={s.y}
              stroke="rgba(11,27,36,0.35)"
              strokeWidth={1}
            />
            <text
              x={60}
              y={s.y}
              textAnchor="end"
              dominantBaseline="middle"
              className="wc-depth-label"
            >
              {s.depth}m
            </text>
            <text
              x={144}
              y={s.y}
              textAnchor="start"
              dominantBaseline="middle"
              className="wc-temp-label"
            >
              {s.temp.toFixed(2)}°
            </text>
          </g>
        ))}
      </svg>
    </div>
  );
}
