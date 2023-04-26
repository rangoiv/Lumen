
import React from 'react';

export const InstrumentsSwitch = (props) => {
	
	if (!props.instruments){
		return(<div></div>)
	}
	if(props.instruments === -3){
		return(<div><h1>...</h1></div>)
	}
	if(props.instruments === -2){
		return(<div><h1>Couldn't send that file!</h1></div>)
	}
	if(props.instruments === -1){
		return(<div><h1>Backend couldn't handle that file!</h1></div>)
	}
	
	return (
		Object.entries(props.instruments).map(([key, value], index) => {
			if (value === 1) {
				return (
					<div key={index}>
						<h1>{key}</h1>
					</div>
				);}
			return null;
		})
	);
};

const sendFileToBackend = async (file) => {
	const formData = new FormData();
	formData.append('file', file);
	try {
		const response = await fetch('http://127.0.0.1:8000/lumen/api/processFile/', {
			method: 'POST',
			body: formData
		});

		if (response.ok) {
			// Handle successful response here
			console.log('File uploaded successfully');
			const jsonResponse = await response.json();
			return jsonResponse
		} else {
			// Handle error response here
			console.error('Failed to upload file!', (await response.text()).toString());
			return -1
		}
	}
	catch (error) {
	// Handle network error here
		console.error('Failed to upload file', error);
		return -2
	}
};

export default sendFileToBackend



