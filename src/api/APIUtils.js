const BACKEND_URL = 'http://localhost:5000/'

export const processMarkersFile = async (formData) => {
    const response = await fetch(BACKEND_URL + '/upload', 
    {
        method: 'POST',
        body: formData,
    })
    const data = await response.json()
    return data
}