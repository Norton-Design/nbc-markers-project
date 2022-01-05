function MarkerError(props) {
    return (
        <div className="flex flex-col border border-gray-500 p-4 rounded-md mx-6 max-w-md">
            <h2 className="mb-3">This file is: <em className="bold text-white bg-red-800 p-2 rounded-md ml-2">INVALID</em></h2>
            <dt className="underline">Error Message:</dt>
            <dd className="italic mt-2">"{props.data.message}"</dd>
        </div>
    )
}

export default MarkerError;