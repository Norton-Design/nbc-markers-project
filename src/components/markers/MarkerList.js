import Marker from "./Marker";

function MarkerList(props) {
    return (
        <div className="flex flex-col border border-gray-500 p-4 rounded-md mx-6">
            <h2 className="mb-3">This file is: <em className="bold text-white bg-green-800 p-2 rounded-md ml-2">VALID</em></h2>
            <p>Asset Title: {props.data.asset_title}</p>
            <p>Asset ID: {props.data.asset_id}</p>
            <p>Asset ID: {props.data.material_type}</p>
            <ul className="mt-3 flex flex-col">
                <h4 className="underline">Markers:</h4>
                { props.data.markers.map((times, i) => <Marker key={i} times={times}/>) }
            </ul>
        </div>
    )
}

export default MarkerList;