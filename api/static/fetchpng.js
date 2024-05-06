async function fetch_data(){
    const resp = await fetch("/fetchpng");
    const data = await resp.json();
    
}