struct Stu{   
    int  m_nSign;
	char m_strName[50]; //学生基本信息 
	char m_strGrade[20];
	char m_strClass[20];
	int  m_nMath; //各科成绩及对应排名
	int  m_nChinese;
	int  m_nEnglish;
	int  m_nComputer;
	Stu *m_pNext;
};
