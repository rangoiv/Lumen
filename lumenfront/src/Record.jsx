import React, { useState, useEffect } from 'react';
import "./styles/Pulse.css"
import sendFileToBackend, {InstrumentsSwitch} from './sendFileToBackend';
import fixWebmDuration from "fix-webm-duration";

var mediaRecorder;
var mediaParts;
var startTime;

const Record = () => {
	
	const [isRecording, setIsRecording] = useState(false);
	const [instruments, setInstruments] = useState(null);
	const [hasMicAccess, setHasMicAccess] = useState(false);

	useEffect(() => {


		const handleDeviceChange = async () => {
			try {
				await navigator.mediaDevices.getUserMedia({ audio: true });
				setHasMicAccess(true);
			} catch (error) {
				setHasMicAccess(false);
				console.error('Failed to access microphone', error);
			}
		};
		handleDeviceChange()
		navigator.mediaDevices.addEventListener('devicechange', handleDeviceChange);
		return () => {
			navigator.mediaDevices.removeEventListener('devicechange', handleDeviceChange);
		};
	}, []);
	const downloadFile = (file) => {
		const blobUrl = URL.createObjectURL(file);
		const link = document.createElement('a');
		link.href = blobUrl;
		link.download = file.name;
		document.body.appendChild(link);
		link.click();
		document.body.removeChild(link);
	};

	function startRecording(stream, options) {
		mediaParts = [];
		mediaRecorder = new MediaRecorder(stream, options);
		mediaRecorder.onstop = function() {
			
			var duration = Date.now() - startTime;
			var buggyBlob = new Blob(mediaParts, { type: 'audio/webm' });

			fixWebmDuration(buggyBlob, duration, {logger: false})
				.then(function(fixedBlob) {
					const createdFile = new File([fixedBlob], 'recorded_audio.webm', { type: 'audio/webm' });
					setInstruments(-3)
					downloadFile(createdFile)
					sendFileToBackend(createdFile).then(result => {	setInstruments(result)})
				});

			
		};
		mediaRecorder.ondataavailable = function(event) {
			var data = event.data;
			if (data && data.size > 0) {
				mediaParts.push(data);
			}
		};
		mediaRecorder.start();
		startTime = Date.now();
	}

	const handleRecordClick = () => {
		navigator.mediaDevices.getUserMedia({ audio: true })
		.then((stream) => 
		{
			setIsRecording(true);
			startRecording(stream, { mimeType: 'audio/webm' })
		})
		.catch((error) => {
			console.error('Failed to access microphone', error);
		});
	};
	
	const handleStopClick = () => {
		mediaRecorder.stop();
		setIsRecording(false);  
	};
	
	return hasMicAccess ? (
		<div className='page'>
		  <img
			src="/src/assets/logo.png"
			alt="Logo"
			style={{ width: '200px', height: '200px', cursor: 'pointer', animation: isRecording ? 'pulse 1s infinite' : 'none'}}
			onClick={isRecording ? handleStopClick : handleRecordClick}
			/>
			<InstrumentsSwitch instruments={instruments}/>
		</div>
	  ) : (<div className='page'><h1>No mic access!</h1></div>);
};
	
export default Record;
	