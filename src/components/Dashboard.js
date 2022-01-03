import {useState, useEffect} from 'react';
import { processMarkersFile } from '../api/APIUtils'

function Dashboard() {
    const [uploadedFile, setUploadedFile] = useState();
    const [isFileSelected, setIsFileSelected] = useState(false);

    const handleFile = (e) => {
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
        // call POST request function here
        const formData = new FormData();
        // console.log(uploadedFile)
        formData.append('file', uploadedFile)
        formData.append('filename', uploadedFile['name'])
        processMarkersFile(formData)
            .then(res => console.log(res))
    }

    return (
        <div>
            <h1>Displaying Editor Dashboard</h1>
            <div>
                <h2>Upload your markers.txt file here:</h2>
                <input type="file" name="file" onChange={handleFile}/>
                { isFileSelected ? 
                    <button onClick={handleFileSubmission}>Submit</button> : 
                    <p>Upload a file to view datails</p> 
                }
                { isFileSelected ? 
                <>
                    <p>Filename: {uploadedFile.name}</p>
                    <p>Filetype: {uploadedFile.type}</p>
                    <p>Size in bytes: {uploadedFile.size}</p>
                </> :
                <></>
                }
            </div>
        </div>
    )
}

export default Dashboard;