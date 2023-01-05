node state{
    has name;
}
walker init{
    spawn here-->node::state(name="Text to Speech");
    spawn here walker::transribe_array;
}
walker transribe_array {
    can stt.transcribe, stt.audio_to_array;
    std.out(here);
    audio_array = stt.audio_to_array("media.mp3");
    report stt.transcribe("en", audio_array);
}