// Copyright (c) 2024, Parwati Bai and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Airline", {
// 	refresh(frm) {

// 	},
// });

// const posturl = `http://parwati.local:8002/api/v2/document/Airline`;

// const newAirline = {
//         "doctype": "airline",
//         "name": "Indian Airlines",
//         "founding_year": 2002,
//         "customer_care_number": 9658741258,
//         "headquarters":  "New Delhi",
// };
// fetch(posturl, {
//     method: 'POST',
//     headers: {
//         "Authorization": "token 872123cb477c4ea:3f229be4bc9f56f",
//         "Content-Type": "application/json"
//     },
//   body: JSON.stringify(newAirline)
// })
// .then(response => response.json())
//   .then(data => {
//     console.log(data);
//   })
//   .catch(error => {
//     console.log(error);
//   });
frappe.ui.form.on('Airline', {
  refresh: function(frm) {
      frm.add_web_link('https://www.example-airline.com','Visit Airline Website');
  }
});
