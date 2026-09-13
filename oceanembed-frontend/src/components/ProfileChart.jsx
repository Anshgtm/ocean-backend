import {
  ResponsiveContainer,
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
} from "recharts";

export default function ProfileChart({ depths, temperatures }) {
  const data = depths.map((d, i) => ({
    depth: d,
    temp: Number(temperatures[i].toFixed(3)),
  }));

  return (
    <div className="profile-chart">
      <ResponsiveContainer width="100%" height={280}>
        <LineChart data={data} margin={{ top: 8, right: 20, left: 0, bottom: 0 }}>
          <CartesianGrid stroke="#1E3B47" strokeDasharray="3 5" />
          <XAxis
            dataKey="depth"
            stroke="#85A0A8"
            tick={{ fill: "#85A0A8", fontSize: 12 }}
            label={{
              value: "Depth (m)",
              position: "insideBottom",
              offset: -2,
              fill: "#85A0A8",
              fontSize: 12,
            }}
          />
          <YAxis
            stroke="#85A0A8"
            tick={{ fill: "#85A0A8", fontSize: 12 }}
            label={{
              value: "°C",
              angle: -90,
              position: "insideLeft",
              fill: "#85A0A8",
              fontSize: 12,
            }}
          />
          <Tooltip
            contentStyle={{
              background: "#102631",
              border: "1px solid #24424F",
              borderRadius: 8,
              fontSize: 12,
              fontFamily: "Inter, sans-serif",
            }}
            labelFormatter={(d) => `${d} m`}
            formatter={(v) => [`${v} °C`, "Temperature"]}
          />
          <Line
            type="monotone"
            dataKey="temp"
            stroke="#FF8659"
            strokeWidth={2}
            dot={{ r: 3, fill: "#FF8659", strokeWidth: 0 }}
            activeDot={{ r: 5 }}
          />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}
