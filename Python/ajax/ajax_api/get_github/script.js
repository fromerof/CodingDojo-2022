function infoGit() {
    fetch("https://api.github.com/users/fromerof")
    .then(response => response.json() )
    .then(coderData => console.log(coderData) )
    .catch(err => console.log(err) )
}

console.log(infoGit.login)

// async function infoGit() {
//     var response = await fetch("https://api.github.com/users/fromerof");
//     var coderData = await response.json();
//     return coderData;
//     }

// console.log(infoGit());
