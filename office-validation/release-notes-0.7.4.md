Ambilight now keeps an independent bounded diagnostic journal for correlating
capture activity with Windows graphics incidents. It records UTC and monotonic
timestamps, process/thread/session and exact source revision, capture operation
intent/completion, GPU adapter/driver identity, first frames and HRESULT/removal
errors, Windows desktop/session/display transitions, device availability and
control actions. Health summaries are recorded every ten seconds.

The journal uses write-through writes and retains eight 4 MiB segments across
restarts. Abrupt-process-exit, append, concurrent writes, retention and I/O-error
regressions are covered. No pixel data, window titles or authentication tokens
are logged. Capture selection, sampling, mapping and output policy are unchanged.

This provides evidence for the next incident; it does not establish the cause of
the earlier graphics-kernel deadlock or promise survival of an incomplete write
during sudden power loss.
