export default function ProfileTable({ depths, temperatures }) {
  return (
    <table className="profile-table">
      <thead>
        <tr>
          <th>Depth</th>
          <th>Temperature</th>
        </tr>
      </thead>
      <tbody>
        {depths.map((d, i) => (
          <tr key={d}>
            <td>{d} m</td>
            <td className="mono">{temperatures[i].toFixed(3)} °C</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
