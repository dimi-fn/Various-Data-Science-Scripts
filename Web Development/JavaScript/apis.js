// Fetch API
fetch("https://type.fit/api/quotes")
  .then((response) => {
    if (!response.ok) {
      throw Error(response.statusText);
    }
    return response.json();
  })
  .then((data) => console.log(data))
  .catch((err) => console.log(err));

  // fetch API with Async/Await 
  /*
  Asynchronous means that the tasks are completed independently and one-by-one like in sychronous tasks
  */
  const fetchData = async () => {
    try {
      const quotes = await fetch("https://type.fit/api/quotes");
      const response = await quotes.json();
      console.log(response);
    } catch (error) {
      console.log(error);
    }
  };
  
  fetchData();
