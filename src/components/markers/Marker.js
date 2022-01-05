function Marker(props) {
    return (
        <li className="">
            <p>{props.times[0]} - {props.times[1]}</p>
        </li>
    )
}

export default Marker;