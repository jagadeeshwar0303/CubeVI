const FACES = ["U", "R", "F", "D", "L", "B"];
const COLOURS = ["W", "R", "G", "Y", "O", "B"];

export default function CubeInput({ value, onChange }) {
  function updateSticker(face, index, colour) {
    // TODO: update exactly one sticker without mutating the existing React state.
    const nextFace = value[face].map((item, i) => (i === index ? colour : item));
    onChange({ ...value, [face]: nextFace });
  }

  return (
    <div className="face-grid">
      {FACES.map((face) => (
        <section className="face-input" key={face}>
          <h3>{face}</h3>
          <div className="sticker-grid">
            {value[face].map((colour, index) => (
              <select key={index} value={colour} onChange={(event) => updateSticker(face, index, event.target.value)}>
                {COLOURS.map((option) => <option key={option}>{option}</option>)}
              </select>
            ))}
          </div>
        </section>
      ))}
    </div>
  );
}

