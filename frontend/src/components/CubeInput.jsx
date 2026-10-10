const faces = ["U", "R", "F", "D", "L", "B"];
const colours = ["W", "R", "G", "Y", "O", "B"];

export default function CubeInput({ value, onChange }) {
  const update = (face, index, colour) => onChange({ ...value, [face]: value[face].map((item, i) => i === index ? colour : item) });
  return <div className="face-grid">{faces.map((face) => <section key={face}><h3>{face}</h3><div className="sticker-grid">{value[face].map((colour, index) => <select key={index} value={colour} onChange={(event) => update(face, index, event.target.value)}>{colours.map((item) => <option key={item}>{item}</option>)}</select>)}</div></section>)}</div>;
}

