use std::time::{Duration, Instant};
use std::{collections::VecDeque, io::Write, path::PathBuf};
extern crate input;

fn main() {
    print!("Input where you want to find the big files here:");
    std::io::stdout().flush().unwrap();
    let mut rustin = input::Input::new();
    let path: PathBuf = rustin.next().unwrap();
    let filesize: u64 = rustin.next().unwrap();
    let start = Instant::now();
    if !path.exists() {
        println!("Path does not exist");
        return;
    }
    let mut q = VecDeque::new();
    q.push_back(path);
    while !q.is_empty() {
        for entry in q.front().unwrap().read_dir().unwrap() {
            if let Ok(entry) = entry {
                if entry.file_type().unwrap().is_file() {
                    if let Ok(metadata) = entry.metadata() {
                        if metadata.len() > filesize {
                            println!("Big file: {}", entry.path().display());
                        }
                    }
                } else if entry.file_type().unwrap().is_dir() {
                    q.push_back(entry.path());
                }
            } else if let Err(err) = entry {
                eprintln!("Error reading directory entry: {}", err);
            }
        }
        q.pop_front();
    }
    let duration = start.elapsed();
    println!("Time taken: {:?}", duration);
}
