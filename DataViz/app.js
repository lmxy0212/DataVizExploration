// const express = require('express');
// const bodyParser = require('body-parser');
// const app = express();
// const PORT = 5500;

// app.use(bodyParser.json());
// app.post('/get_node_description', async (req, res) => {
//   try {
//     const nodeId = req.body.nodeId;
    
//     // Construct the API query here based on your requirement.
//     // Example: Pass nodeId to the ChatGPT API and get the description & keywords
    
//     // Example API call to OpenAI API (pseudo-code)
//     const apiResponse = await fetch('https://api.openai.com/v1/chat/completions', {
//       method: 'POST',
//       headers: {
//         'Content-Type': 'application/json',
//         'Authorization': `Bearer p8BflesHtug2E3dcBx7uT3BlbkFJJH8GRWnSrL54tXs1LAh9`
//       },
//       body: JSON.stringify({
//         model: 'gpt-3.5-turbo',
//         messages: [
//           {role: 'system', content: 'You are a helpful assistant.'},
//           {role: 'user', content: `Tell me about the job: ${nodeId}`}
//         ]
//       })
//     });

//     const apiData = await apiResponse.json();
    
//     // Process the apiData and extract the description and keywords
    
//     // Example (pseudo-code): 
//     const description = "Extracted description from apiData";
//     const keywords = ["keyword1", "keyword2", "keyword3"];
    
//     res.json({
//         description: "Your description here...",
//         keywords: ["keyword1", "keyword2", "keyword3"]
//       });
    
//   } catch (error) {
//     console.error('Error:', error);
//     res.status(500).send('Internal Server Error');
//   }
// });

// app.listen(PORT, () => {
//   console.log(`Server running on http://localhost:${PORT}`);
// });

