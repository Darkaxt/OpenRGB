#pragma once
// SPDX-License-Identifier: GPL-2.0-or-later
// One native state path for the embedded Office caption and activation event.
// Qt 6.8 emulates frameless maximize/restore with MoveWindow; Windows snap and
// system-menu commands use WS_MAXIMIZE. Do not mix those two state owners.
#include <QWidget>
#include <windows.h>

namespace office {
inline void showWindow(QWidget* panel,UINT command=SC_RESTORE) {
    panel->show();
    SendMessageW(reinterpret_cast<HWND>(panel->winId()),WM_SYSCOMMAND,command,0);
}
}
