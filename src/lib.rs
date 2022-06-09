use std::fs;

use pyo3::prelude::*;
use pulldown_cmark::{Parser, html};

// Convert Markdown to HTML.
#[pyfunction]
fn convert(text: &str) -> PyResult<String> {
    let parser = Parser::new(text);

    let mut output = String::new();
    html::push_html(&mut output, parser);

    Ok(output)
}

// Convert Markdown file to HTML.
#[pyfunction]
fn convert_from_file(filename: &str) -> PyResult<String> {
    let content = fs::read_to_string(filename)?;

    convert(&content)
}

/// A Python module implemented in Rust.
#[pymodule]
fn fugue(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(convert, m)?)?;
    m.add_function(wrap_pyfunction!(convert_from_file, m)?)?;
    Ok(())
}
