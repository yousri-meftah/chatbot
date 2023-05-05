async function getBotResponse(input) {
    //rock paper scissors
    //data={"msg":input}
    //console.log(input["msg"])
    

    //console.log(input)
    let res=await fetch("http://127.0.0.1:8000/chatbot",{
        method: 'POST',
        body: JSON.stringify(input),
        mode: 'cors',
        headers: {
        'Content-Type': 'application/json'
        },
    })
    let final =await res.json();
    console.log(final)
    return final['resultat'];

    // Simple responses
    if (input == "hello") {
        return "Hello there!";
    } else if (input == "goodbye") {
        return "Talk to you later!";
    } else {
        return "Try asking something else!";
    }
}