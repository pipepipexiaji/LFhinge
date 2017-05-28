
% @Author: zyc
% @Date:   2017-05-23 12:28:48
% @Last Modified by:   zyc
% @Last Modified time: 2017-05-23 12:28:48
% ########### This script is to generate the profile of E_total versus the whole simulation run time

clc; close all; clear;

% ##### Plot Setting #####
TitleSize=16;
LabelSize=14;
AxisSize=12;
window=1000;

% ###### Real Simulation Time

Simulation_Time = 6.631854e14;
bin=1e5;

fid = dlmread ('/Users/zyc/Dropbox/SharedFolder/NanoHinge-oxDNA/300k60/hinge_energy_60.dat');

timestep = fid (:,1);
E_total = fid (:,4);
Potential = fid(:,2);
E_kinetic = fid(:,3);

xmin=min(timestep);
xmax=max(timestep);
time_unit=Simulation_Time/(xmax-xmin);

Emin=min(E_total);
Emax=max(E_total);

for x=1:5001
    if E_total(x)==Emin
        x;
    end
end

Pmin=min(Potential);
Pmax=max(Potential);

%xtilt=(xmin:bin*time_unit: xmax*time_unit);

%ft = fittype( 'piecewiseLine( x, a, b, c, d, k )' );
%f=fittype('smoothingspline(timestep*time_unit, E_total)');
%figure( 'Name', 'Energy_Distribution');
x=timestep*time_unit;
figure
plot(x, E_total,'k','Linewidth', 2, 'Color', 'blue');
hold on
plot(x,Potential, 'o', 'Linewidth', 3, 'Color','red');
hold off
axis([0 (xmax+10000)*time_unit Pmin-0.01 Emax+0.01])
xlabel('Time (fs)', 'FontSize', 18)
ylabel('Total Energy', 'FontSize', 18)

 


