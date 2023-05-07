
import React from 'react';

import celloImg from './assets/cello.png';
import clarinetImg from './assets/clarinet.png';
import fluteImg from './assets/flute.png';
import acousticGuitarImg from './assets/acguitar.png';
import electricGuitarImg from './assets/elguitar.png';
import organImg from './assets/organ.png';
import pianoImg from './assets/piano.png';
import saxophoneImg from './assets/saxophone.png';
import trumpetImg from './assets/trumpet.png';
import violinImg from './assets/violin.png';
import voiceImg from './assets/voice.png';
import "./styles/waiting.css"

const instrumentsImages = {
  "cel": celloImg,
  "cla": clarinetImg,
  "flu": fluteImg,
  "gac": acousticGuitarImg,
  "gel": electricGuitarImg,
  "org": organImg,
  "pia": pianoImg,
  "sax": saxophoneImg,
  "tru": trumpetImg,
  "vio": violinImg,
  "voi": voiceImg,
};

const instrumentsText = {
    "cel" : "cello",
    "cla" : "clarinet",
    "flu" : "flute",
    "gac" : "acoustic guitar",
    "gel" : "electric guitar",
    "org" : "organ",
    "pia" : "piano",
    "sax" : "saxophone",
    "tru" : "trumpet",
    "vio" : "violin",
    "voi" : "voice",
}

export const InstrumentsSwitch = (props) => {
	
	

	if (!props.instruments){
		return(<div></div>)
	}
	if(props.instruments === -3){
		return(
			<div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', flexDirection: 'row'}}>
				<h1 className="dotW dotW1">.</h1>
				<h1 className="dotW dotW2">.</h1>
				<h1 className="dotW dotW3">.</h1>
			</div>
		)
	}
	if(props.instruments === -2){
		return(<div><h1>Couldn't send that file!</h1></div>)
	}
	if(props.instruments === -1){
		return(<div><h1>Backend couldn't handle that file!</h1></div>)
	}
	
	return (
		<div>
		<h2 style={{ fontSize: '24px', marginRight: '16px' }}>Your instruments are:</h2>	
		{
		Object.entries(props.instruments).map(([key, value], index) => {
			if (value === 1) {
				return (
					<div key={index} >
						<img src={instrumentsImages[key]} alt={instrumentsText[key]} style={{ width: '50px', borderRadius: '50%', marginBottom: '16px' }} />
					</div>
				);}
			return null;
		})
		}</div>
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



