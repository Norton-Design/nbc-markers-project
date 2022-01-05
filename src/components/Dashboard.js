import { useState } from 'react';
import { processMarkersFile } from '../api/APIUtils'
import MarkerError from './markers/MarkerError';
import MarkerList from './markers/MarkerList';

function Dashboard() {
    const [uploadedFile, setUploadedFile] = useState();
    const [isFileSelected, setIsFileSelected] = useState(false);
    const [validatedData, setValidatedData] = useState(false)
    const [error, setError] = useState(false)

    const handleFile = (e) => {
        setValidatedData(false)
        setError(false)
        const file = e.target.files[0]
        if (file){
            if (file.type === 'text/plain'){
                setUploadedFile(file)
                setIsFileSelected(true)
            } else {
                e.target.value = null
                alert("File type must be .txt")
            }
        }
    }

    const handleFileSubmission = () => {
        const formData = new FormData();
        formData.append('file', uploadedFile)
        formData.append('filename', uploadedFile['name'])
        processMarkersFile(formData)
            .then(res => {
                if (res.error){
                    setError(res)
                } else {
                    setValidatedData(res)
                }
            })
    }

    return (
        <div className="min-w-screen min-h-[80vh] bg-gray-100 flex flex-col justify-center items-center">
            <h1 className="text-4xl mb-7">Marker Validation Dashboard</h1>
            <div className="flex flex-row justify-center items-center">
                <div className="flex flex-col border border-gray-500 p-4 rounded-md mx-6">
                    <p className="mb-2">Upload your markers.txt file here:</p>
                    <input className="hidden" type="file" id="selectFile" name="file" onChange={handleFile}/>
                    <input 
                        type="button"  
                        value="Choose your file" 
                        onClick={()=>document.getElementById('selectFile').click()} 
                        className="p-2 bg-gray-300 border border-gray-500 rounded-lg"
                    />
                    { isFileSelected ? 
                        <div className="mt-4">
                            <h4>File Details</h4>
                            <p>Filename: {uploadedFile.name}</p>
                            <p>Filetype: {uploadedFile.type}</p>
                            <p>Size in bytes: {uploadedFile.size}</p>
                        </div> :
                        <></>
                    }
                    { isFileSelected ? 
                        <button 
                            className="p-2 bg-green-500 text-white border border-green-800 rounded-lg mt-4"
                            onClick={handleFileSubmission}>Validate
                        </button> : 
                        <></> 
                    }
                </div>
                { validatedData ? <MarkerList data={validatedData}/> : <></> }
                { error ? <MarkerError data={error}/> : <></>}
            </div>
        </div>
    )
}

export default Dashboard;