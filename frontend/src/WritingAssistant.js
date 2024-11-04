//version1
import React, { useState } from 'react';
import axios from 'axios';
import './WritingAssistant.css';

function WritingAssistant() {
    const [inputText, setInputText] = useState('');
    const [result, setResult] = useState('');
    const [task, setTask] = useState('grammar_correction');
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false);

    //Text processing
    const handleProcessText = async () => {
        setLoading(true);
        setError('');
        setResult('');
        
        try {
            const response = await axios.post('http://localhost:8000/process_text/', {
                text: inputText,
                task: task
            });
            setResult(response.data.result);
        } catch (error) {
            console.error('Error processing text:', error);
            setError('Failed to process text. Please try again.');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="writing-assistant-container">
            <h1>Virtual Writing Assistant</h1>
            
            <textarea 
                className="textarea"
                value={inputText}
                onChange={(e) => setInputText(e.target.value)}
                placeholder="Enter your text here..."
                rows={5}
            />

            <select 
                className="select"
                onChange={(e) => setTask(e.target.value)} 
                value={task}
            >
                <option value="grammar_correction">Grammar Correction</option>
                <option value="style_enhancement">Style Enhancement</option>
                <option value="tone_adjustment">Tone Adjustment</option>
            </select>

            <button 
                className="button" 
                onClick={handleProcessText}
                disabled={loading}
            >
                {loading ? 'Processing...' : 'Process Text'}
            </button>

            {error && <div className="error">{error}</div>}

            <div className="result-container">
                <h2>Result:</h2>
                <p className="result">{result}</p>
            </div>
        </div>
    );
}

export default WritingAssistant;


