/*
OpenChrono
Copyright (C) 2007  Sebastien CELLES
 
This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.
 
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
 
You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
*/

#ifndef MESSAGEIMPL_H
#define MESSAGEIMPL_H
//
#include "ui_message.h"
//
#include "data.h"

#include <QString>

class MessageImpl : public QDialog, public Ui::frmMessage
  {
    Q_OBJECT

  public:
    MessageImpl( QWidget * parent = 0, Qt::WFlags f = 0); //, Data * data = 0 );

  public slots:
    void setTitle(QString str);
    void setMessage(QString str);

    //private:
    //Data * m_Data;
  };
#endif
