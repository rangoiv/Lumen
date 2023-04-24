import React, { useState } from 'react';
import Button from '@mui/material/Button';
import CloudUploadIcon from '@mui/icons-material/CloudUpload';
import sendFileToBackend, {InstrumentsSwitch} from './sendFileToBackend';

import logo from './assets/logo.png';
import "./styles/Wrapper.css"

function FrontPage() {
	const [file, setFile] = useState(null);
	const [instruments, setInstruments] = useState(null);
	
	const handleSubmit = async (e) => {
		e.preventDefault();
		if (file) {
			setInstruments(-3)
			var result = await sendFileToBackend(file)
			setInstruments(result)
		}
	};
	
	const handleFileChange = (e) => {
		setInstruments(0)
		setFile(e.target.files[0]);
	};
	
	const handleDragOver = (e) => {
		e.preventDefault();
	};
	
	const handleDrop = (e) => {
		e.preventDefault();
		setFile(e.dataTransfer.files[0]);
	};
	
	return (
		<div className='page'>
			<img src={logo} alt="Logo" style={{ width: '50px', borderRadius: '50%', marginBottom: '16px' }} />
			<form onSubmit={handleSubmit} encType="multipart/form-data" style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
				<label htmlFor="file">
					<input accept="audio/*" id="file" type="file" style={{ display: 'none' }} onChange={handleFileChange}/>
					<Button variant="outlined" component="span" startIcon={<CloudUploadIcon />} style={{ marginBottom: '16px' }}>
						{file ? file.name : "Submit a song"}
					</Button>
				</label>
				<Button type="submit" variant="contained" color="primary" disabled={!file} style={{ backgroundColor: '#4D545A', color: 'White' }}>
					Submit
				</Button>
			</form>
			<InstrumentsSwitch instruments={instruments}/>
		</div>
		);
	};
	
	export default FrontPage;