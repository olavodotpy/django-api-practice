async function bodyAPI() {
    try {
        const response = await fetch('./data.json');
        const r = await response.json();
        return r.body;
    } catch (error) {
        console.error('Error to get the JSON file', error);
        return undefined;
    }
}


bodyAPI().then(body => {
    const HTMLText = document.getElementById("APIText");
    HTMLText.innerText = body;
});
